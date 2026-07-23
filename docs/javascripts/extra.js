document.addEventListener("DOMContentLoaded", function () {
  const tagDataScript = document.getElementById("tag-data");
  const searchInput = document.getElementById("tag-search-input");
  const activeBar = document.getElementById("active-filters-bar");
  const activeChipsContainer = document.getElementById("active-tags-chips");
  const clearBtn = document.getElementById("clear-tags-btn");
  const countBadge = document.getElementById("filter-count-badge");
  const tagCloud = document.getElementById("tag-cloud-container");
  const resultsContainer = document.getElementById("tag-results-container");

  if (!tagDataScript || !searchInput || !resultsContainer) return;

  let articles = [];
  try {
    articles = JSON.parse(tagDataScript.textContent || "[]");
  } catch (e) {
    console.error("Failed to parse tag-data JSON", e);
    return;
  }

  const selectedTags = new Set();
  const staticHtml = resultsContainer.innerHTML;

  function renderResults() {
    if (selectedTags.size === 0) {
      activeBar.style.display = "none";
      resultsContainer.innerHTML = staticHtml;
      updateTagPillsState();
      return;
    }

    // Show active filter bar
    activeBar.style.display = "flex";
    activeChipsContainer.innerHTML = "";

    selectedTags.forEach(function (tag) {
      const chip = document.createElement("button");
      chip.type = "button";
      chip.className = "active-chip";
      chip.innerHTML = `<span>${tag}</span> <span class="chip-remove">×</span>`;
      chip.addEventListener("click", function () {
        selectedTags.delete(tag);
        renderResults();
      });
      activeChipsContainer.appendChild(chip);
    });

    // Filter articles that contain ALL selected tags
    const matchingArticles = articles.filter(function (art) {
      const artTagSet = new Set(art.tags);
      for (let reqTag of selectedTags) {
        if (!artTagSet.has(reqTag)) return false;
      }
      return true;
    });

    countBadge.textContent = `Showing ${matchingArticles.length} guide${matchingArticles.length !== 1 ? "s" : ""} matching all filters`;

    if (matchingArticles.length === 0) {
      resultsContainer.innerHTML = `
        <div class="no-results-box">
          <h3>No matching guides found</h3>
          <p>No routes or guides match all of your selected tags (${Array.from(selectedTags).join(", ")}). Try removing a tag or clearing your filters.</p>
        </div>
      `;
    } else {
      let html = `<div class="tag-filtered-grid">`;
      matchingArticles.forEach(function (art) {
        const tagBadges = art.tags
          .map(function (t) {
            const isActive = selectedTags.has(t) ? "active-badge" : "";
            return `<span class="article-tag-badge ${isActive}" data-tag="${t.replace(/"/g, "&quot;")}">${t}</span>`;
          })
          .join(" ");

        html += `
          <div class="article-card">
            <h3 class="article-card-title"><a href="${art.url}">${art.title}</a></h3>
            <div class="article-card-tags">${tagBadges}</div>
          </div>
        `;
      });
      html += `</div>`;
      resultsContainer.innerHTML = html;

      // Add click listeners to tag badges inside result cards
      resultsContainer.querySelectorAll(".article-tag-badge").forEach(function (btn) {
        btn.addEventListener("click", function () {
          const t = btn.getAttribute("data-tag");
          if (t) {
            if (selectedTags.has(t)) {
              selectedTags.delete(t);
            } else {
              selectedTags.add(t);
            }
            renderResults();
          }
        });
      });
    }

    updateTagPillsState();
  }

  function updateTagPillsState() {
    if (!tagCloud) return;
    const buttons = tagCloud.querySelectorAll(".tag-pill-btn");
    buttons.forEach(function (btn) {
      const tag = btn.getAttribute("data-tag");
      if (selectedTags.has(tag)) {
        btn.classList.add("active");
      } else {
        btn.classList.remove("active");
      }
    });
  }

  // Filter tag cloud buttons via search input
  searchInput.addEventListener("input", function (e) {
    const q = (e.target.value || "").toLowerCase().trim();
    if (!tagCloud) return;
    const buttons = tagCloud.querySelectorAll(".tag-pill-btn");
    buttons.forEach(function (btn) {
      const tag = (btn.getAttribute("data-tag") || "").toLowerCase();
      if (!q || tag.includes(q)) {
        btn.style.display = "inline-flex";
      } else {
        btn.style.display = "none";
      }
    });
  });

  // Toggle tag selection on click
  if (tagCloud) {
    tagCloud.addEventListener("click", function (e) {
      const btn = e.target.closest(".tag-pill-btn");
      if (!btn) return;
      const tag = btn.getAttribute("data-tag");
      if (!tag) return;

      if (selectedTags.has(tag)) {
        selectedTags.delete(tag);
      } else {
        selectedTags.add(tag);
      }
      renderResults();
    });
  }

  // Clear all button
  if (clearBtn) {
    clearBtn.addEventListener("click", function () {
      selectedTags.clear();
      searchInput.value = "";
      // Reset search filter display
      if (tagCloud) {
        tagCloud.querySelectorAll(".tag-pill-btn").forEach(function (b) {
          b.style.display = "inline-flex";
        });
      }
      renderResults();
    });
  }
});
