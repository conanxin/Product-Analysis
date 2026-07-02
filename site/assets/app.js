/* Product Analysis — GitHub Pages Showcase */
/* Source-first static JS — no external CDN, no network calls beyond products.json */

(function () {
  "use strict";

  var BLOB_BASE = "https://github.com/conanxin/Product-Analysis/blob/master/";

  function blobHref(repoRelativePath) {
    return BLOB_BASE + repoRelativePath;
  }

  function escapeHtml(s) {
    if (s === null || s === undefined) return "";
    return String(s).replace(/[&<>"']/g, function (c) {
      return ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
      })[c];
    });
  }

  function makeBadge(label, kind, value) {
    var safeLabel = escapeHtml(label);
    var safeKind = escapeHtml(kind);
    var safeValue = escapeHtml(value);
    return '<span class="badge ' + safeKind + '" title="' + safeValue + '">' + safeLabel + '</span>';
  }

  function renderProductCard(p) {
    var tagsHtml = (p.tags || []).slice(0, 4).map(function (t) {
      return '<span class="tag">' + escapeHtml(t) + '</span>';
    }).join("");

    var reviewedBadge = makeBadge("reviewed", "reviewed", "人工复核完成");
    var partialBadge = makeBadge("partial", "partial", "来源验证状态 partial");

    return (
      '<article class="product-card" data-category="' + escapeHtml(p.category_key) + '" data-name="' + escapeHtml(p.name).toLowerCase() + '" data-tags="' + escapeHtml((p.tags || []).join(" ").toLowerCase()) + '">' +
        '<div class="name">' + escapeHtml(p.name) + '</div>' +
        '<div class="category">' + escapeHtml(p.category) + '</div>' +
        '<div class="insight">' + escapeHtml(p.one_line) + '</div>' +
        (tagsHtml ? '<div class="tags">' + tagsHtml + '</div>' : '') +
        '<div class="meta">' + reviewedBadge + partialBadge + '</div>' +
        '<a class="read-link" href="' + escapeHtml(blobHref(p.file)) + '" target="_blank" rel="noopener">Read analysis →</a>' +
      '</article>'
    );
  }

  function renderFallbackList(products) {
    return products.map(function (p) {
      return '<li><a href="' + escapeHtml(blobHref(p.file)) + '" target="_blank" rel="noopener">' + escapeHtml(p.name) + '</a> — ' + escapeHtml(p.one_line) + '</li>';
    }).join("");
  }

  function renderLandscape(landscape) {
    return landscape.map(function (g) {
      var items = g.products.map(function (name) {
        return '<li>' + escapeHtml(name) + '</li>';
      }).join("");
      return (
        '<div class="landscape-group">' +
          '<h3>' + escapeHtml(g.category) + '</h3>' +
          '<ul>' + items + '</ul>' +
        '</div>'
      );
    }).join("");
  }

  function applyFilters(state, products) {
    var q = (state.query || "").trim().toLowerCase();
    var activeCat = state.category || "all";
    var cards = document.querySelectorAll(".product-card");
    var visibleCount = 0;

    cards.forEach(function (card) {
      var cat = card.getAttribute("data-category") || "";
      var name = card.getAttribute("data-name") || "";
      var tags = card.getAttribute("data-tags") || "";
      var matchesCat = activeCat === "all" || cat === activeCat;
      var matchesQuery = !q || name.indexOf(q) !== -1 || cat.indexOf(q) !== -1 || tags.indexOf(q) !== -1;

      if (matchesCat && matchesQuery) {
        card.classList.remove("hidden");
        visibleCount++;
      } else {
        card.classList.add("hidden");
      }
    });

    var countEl = document.getElementById("visible-count");
    if (countEl) {
      countEl.textContent = visibleCount + " / " + products.length + " products";
    }
  }

  function init(data) {
    var products = data.products || [];
    var summary = data.summary || {};
    var landscape = data.landscape || [];

    var summaryTotal = document.getElementById("summary-total");
    if (summaryTotal) summaryTotal.textContent = (summary.total || products.length) + " reviewed AI analyses";

    var landscapeEl = document.getElementById("product-landscape");
    if (landscapeEl) landscapeEl.innerHTML = renderLandscape(landscape);

    var gridEl = document.getElementById("product-grid");
    if (gridEl) gridEl.innerHTML = products.map(renderProductCard).join("");

    var fallbackEl = document.getElementById("product-fallback-list");
    if (fallbackEl) fallbackEl.innerHTML = renderFallbackList(products);

    var state = { query: "", category: "all" };

    var searchEl = document.getElementById("search-input");
    if (searchEl) {
      searchEl.addEventListener("input", function (e) {
        state.query = e.target.value || "";
        applyFilters(state, products);
      });
    }

    var filterButtons = document.querySelectorAll(".filter-btn");
    filterButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var cat = btn.getAttribute("data-category") || "all";
        state.category = cat;
        filterButtons.forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        applyFilters(state, products);
      });
    });

    applyFilters(state, products);
  }

  function loadData() {
    var url = "data/products.json";
    fetch(url, { cache: "no-cache" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status + " loading " + url);
        return r.json();
      })
      .then(init)
      .catch(function (err) {
        console.error("[product-analysis] failed to load products.json:", err);
        var fallbackEl = document.getElementById("product-fallback-list");
        var fallbackWrap = document.getElementById("product-fallback");
        if (fallbackEl && fallbackWrap) {
          fallbackWrap.classList.remove("no-js-fallback");
          fallbackEl.innerHTML = '<li style="color: var(--red);">Failed to load product data: ' + escapeHtml(err.message) + '. Please check that data/products.json exists.</li>';
        }
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", loadData);
  } else {
    loadData();
  }
})();