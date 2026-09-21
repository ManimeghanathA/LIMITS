const state = {
  source: "manual",
  budget: 256,
  contents: [],
  running: false,
};

const contentBox = document.querySelector("#contentBox");
const questionPanel = document.querySelector("#questionPanel");
const questionSelect = document.querySelector("#questionSelect");
const questionBox = document.querySelector("#questionBox");
const runButton = document.querySelector("#runButton");
const stage = document.querySelector("#stage");
const stageTitle = document.querySelector("#stageTitle");
const stageCopy = document.querySelector("#stageCopy");
const progressFill = document.querySelector("#progressFill");
const paragraphRail = document.querySelector("#paragraphRail");
const scoreBody = document.querySelector("#scoreBody");
const interactionList = document.querySelector("#interactionList");
const subsetBody = document.querySelector("#subsetBody");
const breakdown = document.querySelector("#breakdown");
const finalContext = document.querySelector("#finalContext");

async function boot() {
  const response = await fetch("/api/contents");
  const payload = await response.json();
  state.contents = payload.contents;
  bindEvents();
  updateQuestionAvailability();
}

function bindEvents() {
  document.querySelectorAll(".source-button").forEach((button) => {
    button.addEventListener("click", () => setSource(button.dataset.source));
  });
  document.querySelectorAll(".budget-button").forEach((button) => {
    button.addEventListener("click", () => {
      state.budget = Number(button.dataset.budget);
      document.querySelectorAll(".budget-button").forEach((item) => item.classList.remove("active"));
      button.classList.add("active");
    });
  });
  contentBox.addEventListener("input", updateQuestionAvailability);
  questionBox.addEventListener("input", updateRunAvailability);
  questionSelect.addEventListener("change", () => {
    if (questionSelect.value === "manual") {
      questionBox.value = "";
      questionBox.disabled = false;
      questionBox.focus();
    } else {
      const item = activeContent()?.questions.find((question) => question.id === questionSelect.value);
      questionBox.value = item?.text ?? "";
      questionBox.disabled = true;
    }
    updateRunAvailability();
  });
  runButton.addEventListener("click", runKnapsack);
}

function setSource(source) {
  state.source = source;
  document.querySelectorAll(".source-button").forEach((button) => {
    button.classList.toggle("active", button.dataset.source === source);
  });
  if (source === "manual") {
    contentBox.value = "";
    contentBox.readOnly = false;
    contentBox.placeholder = "Paste or write paragraphs here. Separate paragraphs with a blank line.";
    renderQuestionOptions([]);
    questionBox.value = "";
    questionBox.disabled = false;
  } else {
    const content = activeContent();
    contentBox.value = content.text;
    contentBox.readOnly = false;
    renderQuestionOptions(content.questions);
    questionSelect.value = content.questions[0]?.id ?? "manual";
    questionBox.value = content.questions[0]?.text ?? "";
    questionBox.disabled = true;
  }
  updateQuestionAvailability();
}

function activeContent() {
  return state.contents.find((content) => content.key === state.source);
}

function renderQuestionOptions(questions) {
  questionSelect.innerHTML = "";
  const manual = document.createElement("option");
  manual.value = "manual";
  manual.textContent = "Manual question";
  questionSelect.appendChild(manual);
  questions.forEach((question) => {
    const option = document.createElement("option");
    option.value = question.id;
    option.textContent = `${question.category.replace("_", " ")} - ${question.text}`;
    questionSelect.appendChild(option);
  });
  questionSelect.disabled = questions.length === 0;
}

function updateQuestionAvailability() {
  const hasContent = contentBox.value.trim().length > 0;
  questionPanel.classList.toggle("disabled", !hasContent);
  questionBox.disabled = !hasContent || (state.source !== "manual" && questionSelect.value !== "manual");
  if (state.source === "manual") {
    questionSelect.disabled = true;
  }
  updateRunAvailability();
}

function updateRunAvailability() {
  runButton.disabled = state.running || !contentBox.value.trim() || !questionBox.value.trim();
}

async function runKnapsack() {
  state.running = true;
  updateRunAvailability();
  runButton.classList.add("loading");
  runButton.textContent = "Computing";
  stage.classList.remove("hidden");
  resetStage();
  stage.scrollIntoView({ behavior: "smooth", block: "start" });
  try {
    const response = await fetch("/api/trace", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        source: state.source,
        content: contentBox.value,
        question: questionBox.value,
        budget: state.budget,
      }),
    });
    const trace = await response.json();
    if (!response.ok) {
      throw new Error(trace.error || "Trace failed");
    }
    await animateTrace(trace);
  } catch (error) {
    stageTitle.textContent = "Could not run knapsack";
    stageCopy.textContent = error.message;
  } finally {
    state.running = false;
    runButton.classList.remove("loading");
    runButton.textContent = "Run Knapsack";
    updateRunAvailability();
  }
}

function resetStage() {
  stageTitle.textContent = "Preparing candidate paragraphs";
  stageCopy.textContent = "Paragraphs enter the selector, then the 15-candidate pool is built.";
  progressFill.style.width = "0%";
  paragraphRail.innerHTML = "";
  scoreBody.innerHTML = "";
  interactionList.innerHTML = "";
  subsetBody.innerHTML = "";
  breakdown.innerHTML = "";
  finalContext.innerHTML = "";
}

async function animateTrace(trace) {
  stageTitle.textContent = "Paragraph intake";
  stageCopy.textContent = "Every paragraph becomes a candidate chunk with a token cost.";
  renderParagraphs(trace.paragraphs, [], []);
  progressFill.style.width = "15%";
  await wait(900);

  stageTitle.textContent = "Selecting the 15-candidate pool";
  stageCopy.textContent = "The selector mixes sparse query overlap, semantic similarity, and seed linkage.";
  renderParagraphs(trace.paragraphs, trace.candidates.map((item) => item.id), []);
  progressFill.style.width = "32%";
  await wait(950);

  stageTitle.textContent = "Filling the value table";
  stageCopy.textContent = "Each row is a public feature calculation used by the knapsack utility.";
  renderScoreRows(trace.scoreRows);
  progressFill.style.width = "52%";
  await wait(1100);

  stageTitle.textContent = "Adding pair, triple, and redundancy terms";
  stageCopy.textContent = "Connected chunks receive synergy; repeated chunks receive penalties.";
  renderInteractions(trace.interactionRows);
  progressFill.style.width = "68%";
  await wait(1100);

  stageTitle.textContent = "Running exact knapsack search";
  stageCopy.textContent = "Feasible subsets compete under the selected token budget.";
  renderSubsetRows(trace.subsetRows);
  progressFill.style.width = "84%";
  await wait(1200);

  stageTitle.textContent = "Optimal context selected";
  stageCopy.textContent = `${trace.final.selectedIds.length} paragraphs selected, ${trace.final.tokenUsed}/${trace.budget} tokens used.`;
  renderBreakdown(trace.breakdown, trace.final);
  renderParagraphs(trace.paragraphs, trace.candidates.map((item) => item.id), trace.final.selectedIds);
  renderFinalContext(trace.paragraphs, trace.final.selectedIds);
  progressFill.style.width = "100%";
}

function renderParagraphs(paragraphs, candidateIds, selectedIds) {
  const candidateSet = new Set(candidateIds);
  const selectedSet = new Set(selectedIds);
  paragraphRail.innerHTML = "";
  paragraphs.forEach((paragraph, index) => {
    const card = document.createElement("article");
    card.className = "para-card";
    if (candidateSet.has(paragraph.id)) card.classList.add("candidate");
    if (selectedSet.has(paragraph.id)) card.classList.add("selected");
    card.style.animationDelay = `${Math.min(index * 28, 500)}ms`;
    card.innerHTML = `
      <span class="para-id">${paragraph.id} · ${paragraph.tokens} tok</span>
      <p class="para-text">${escapeHtml(paragraph.text)}</p>
    `;
    paragraphRail.appendChild(card);
  });
}

function renderScoreRows(rows) {
  scoreBody.innerHTML = "";
  rows.forEach((row, index) => {
    const tr = document.createElement("tr");
    tr.style.animationDelay = `${index * 55}ms`;
    tr.innerHTML = `
      <td>${row.rank}</td>
      <td><strong>${row.id}</strong></td>
      <td>${row.tokens}</td>
      <td>${row.queryOverlap.toFixed(3)}</td>
      <td>${row.semanticSimilarity.toFixed(3)}</td>
      <td>${row.tokenPressure.toFixed(3)}</td>
      <td><strong>${row.individualScore.toFixed(3)}</strong></td>
    `;
    scoreBody.appendChild(tr);
  });
}

function renderInteractions(rows) {
  interactionList.innerHTML = "";
  const groups = [
    ["Pair synergy", rows.pairSynergy.slice(0, 6), "score"],
    ["Redundancy penalty", rows.redundancy.slice(0, 5), "penalty"],
    ["Triple synergy", rows.tripleSynergy.slice(0, 5), "score"],
  ];
  groups.forEach(([label, items, key], groupIndex) => {
    const title = document.createElement("div");
    title.className = "pill-row";
    title.style.animationDelay = `${groupIndex * 120}ms`;
    title.innerHTML = `<span>${label}</span><strong>${items.length}</strong>`;
    interactionList.appendChild(title);
    items.forEach((item, index) => {
      const row = document.createElement("div");
      row.className = "pill-row";
      row.style.animationDelay = `${180 + (groupIndex * 5 + index) * 70}ms`;
      row.innerHTML = `<span>${item.ids.join(" + ")}</span><strong>${Number(item[key]).toFixed(3)}</strong>`;
      interactionList.appendChild(row);
    });
  });
}

function renderSubsetRows(rows) {
  subsetBody.innerHTML = "";
  rows.slice(0, 34).forEach((row, index) => {
    const tr = document.createElement("tr");
    tr.style.animationDelay = `${index * 45}ms`;
    const statusClass = row.status === "final best" ? "status-final" : row.status === "current best" ? "status-best" : "";
    tr.innerHTML = `
      <td>${row.ids.length ? row.ids.join(" + ") : "empty"}</td>
      <td>${row.tokenCost}</td>
      <td>${row.utility === null ? "-" : Number(row.utility).toFixed(3)}</td>
      <td><span class="subset-status ${statusClass}">${row.status}</span></td>
    `;
    subsetBody.appendChild(tr);
  });
}

function renderBreakdown(items, final) {
  breakdown.innerHTML = "";
  const rows = [
    ["Individual sum", items.individual],
    ["Pair synergy", items.pairSynergy],
    ["Triple synergy", items.tripleSynergy],
    ["Redundancy penalty", -items.redundancyPenalty],
    ["Total utility", items.total],
    ["Token usage", final.tokenUsed],
  ];
  rows.forEach(([label, value], index) => {
    const row = document.createElement("div");
    row.className = "metric-row";
    row.style.animationDelay = `${index * 90}ms`;
    row.innerHTML = `<span>${label}</span><strong>${Number(value).toFixed(3)}</strong>`;
    breakdown.appendChild(row);
  });
}

function renderFinalContext(paragraphs, selectedIds) {
  const byId = new Map(paragraphs.map((paragraph) => [paragraph.id, paragraph]));
  finalContext.innerHTML = "";
  selectedIds.forEach((id, index) => {
    const paragraph = byId.get(id);
    if (!paragraph) return;
    const card = document.createElement("div");
    card.className = "final-para";
    card.style.animationDelay = `${index * 120}ms`;
    card.innerHTML = `<strong>${paragraph.id}</strong><p>${escapeHtml(paragraph.text)}</p>`;
    finalContext.appendChild(card);
  });
}

function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function escapeHtml(text) {
  return text.replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#039;",
  }[char]));
}

boot();
