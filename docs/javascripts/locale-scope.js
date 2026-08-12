// Scopes two of Material's built-in features to the current page's
// language: search, and the "Download PDF" footer link.
//
// mkdocs-static-i18n builds every locale into a single site, and Material's
// generated assets are shared site-wide (one search_index.json, one PDF
// link target per config) -- so both need a client-side correction to
// point at the right locale's version instead. hooks/split_search_index.py
// and scripts/build_pdfs.py produce the per-locale files this reads; the
// locale list below is patched in by the former after the build (empty
// here is just the pre-build placeholder).
//
// The version (mike) axis doesn't need any of this: mike builds and deploys
// each version to its own subtree with its own independent search index and
// PDFs, so there's no cross-version bleed to begin with -- both fixups below
// resolve relative to the *current* version's own site root (`base`, read
// from Material's own `#__config` script tag) rather than a hardcoded path.
(function () {
  var locales = /*__I18N_LOCALES__*/ [];
  if (!locales.length) {
    return;
  }

  var localeMatch = location.pathname.match(
    new RegExp("/(" + locales.join("|") + ")(?:/|$)")
  );
  var locale = localeMatch ? localeMatch[1] : "en";

  scopeSearchIndex(locale);
  scopePdfLink(locale);

  // Scopes Material's built-in search to `locale`.
  //
  // Material's search plugin combines every locale's pages into one
  // search_index.json (see mkdocs_static_i18n's
  // plugin.reconfigure_search_index) -- so out of the box, searching from an
  // English page also surfaces French/German/... results. There's no config
  // knob for this -- see
  // https://github.com/ultrabug/mkdocs-static-i18n/issues/271.
  //
  // This rewrites the one XHR Material's bundle.js makes for
  // search_index.json to fetch the split file matching `locale` instead,
  // before that request fires. overrides/main.html loads this script
  // *before* bundle.js specifically so this patch is in place before that
  // request goes out -- see that file for why.
  function scopeSearchIndex(locale) {
    var originalOpen = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function (method, url) {
      var args = Array.prototype.slice.call(arguments);
      if (typeof url === "string" && /search\/search_index\.json(?:\?|$)/.test(url)) {
        args[1] = url.replace("search_index.json", "search_index-" + locale + ".json");
      }
      return originalOpen.apply(this, args);
    };
  }

  // Points the footer's "Download PDF" link (added via mkdocs.yml's
  // `extra.social`, with a "#" placeholder href -- see there) at
  // `<site root>/<locale>/ethos-manual.pdf`, built from `locale` and
  // Material's own `#__config.base` (its path back to the current version's
  // site root, however deep the current page is nested).
  function scopePdfLink(locale) {
    var configTag = document.getElementById("__config");
    var link = document.querySelector('.md-social__link[title="Download PDF"]');
    if (!configTag || !link) {
      return;
    }
    var base = JSON.parse(configTag.textContent).base;
    var dir = locale === "en" ? base : base + "/" + locale;
    link.href = dir + "/ethos-manual.pdf";
  }
})();
