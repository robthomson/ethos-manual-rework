// Scopes two of Material's built-in features to the current page's
// language: search, and the "Download PDF" footer link.
//
// mkdocs-static-i18n builds every locale into a single site, and Material's
// generated assets are shared site-wide (one search_index.json, one PDF
// link target per config) -- so both need a client-side correction to
// point at the right locale's version instead. The two placeholders below
// are patched in after the build: the locale list by
// hooks/split_search_index.py, the PDF base URL by
// scripts/patch_pdf_links.py (empty here is just the pre-patch default,
// e.g. during `mkdocs serve`).
(function () {
  var locales = /*__I18N_LOCALES__*/ ["cs", "de", "es", "fr", "he", "it", "nb", "nl", "pl", "pt-BR", "zh"];
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
  // `extra.social`, with a "#" placeholder href -- see there) at `locale`'s
  // PDF manual.
  //
  // These are GitHub Release assets, not part of the deployed site -- a
  // ~17MB PDF per locale, regenerated and re-uploaded on every deploy,
  // would otherwise permanently bloat the gh-pages branch's git history
  // every single time (see scripts/build_pdfs.py's docstring). The base
  // URL patched in below already has the release download prefix and tag,
  // so this just appends the per-locale filename.
  function scopePdfLink(locale) {
    var base = /*__PDF_BASE_URL__*/ "";
    var link = document.querySelector('.md-social__link[title="Download PDF"]');
    if (!base || !link) {
      return;
    }
    link.href = base + "ethos-manual-" + locale + ".pdf";
  }
})();
