// Scopes Material's built-in search to the current page's language.
//
// mkdocs-static-i18n builds every locale into a single site, and
// mkdocs-material's search plugin combines every locale's pages into one
// search_index.json (see mkdocs_static_i18n's
// plugin.reconfigure_search_index) -- so out of the box, searching from an
// English page also surfaces French/German/... results. There's no config
// knob for this -- see https://github.com/ultrabug/mkdocs-static-i18n/issues/271.
//
// hooks/split_search_index.py splits that combined index into
// search/search_index-<locale>.json per locale after the build, and patches
// the locale list below in. This rewrites the one XHR Material's bundle.js
// makes for search_index.json to fetch the split file matching the locale
// segment in the current URL, before that request fires. overrides/main.html
// loads this file *before* bundle.js specifically so this patch is in place
// before that request goes out -- see that file for why.
//
// The version (mike) axis doesn't need any of this: mike builds and deploys
// each version to its own subtree with its own independent search index, so
// there's no cross-version bleed to begin with.
//
// Falls back to the stock, unfiltered combined index if the list below is
// still empty -- e.g. during `mkdocs serve` before this hook has run once.
(function () {
  var locales = /*__I18N_LOCALES__*/ [];
  if (!locales.length) {
    return;
  }

  var localeMatch = location.pathname.match(
    new RegExp("/(" + locales.join("|") + ")(?:/|$)")
  );
  var locale = localeMatch ? localeMatch[1] : "en";

  var originalOpen = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function (method, url) {
    var args = Array.prototype.slice.call(arguments);
    if (typeof url === "string" && /search\/search_index\.json(?:\?|$)/.test(url)) {
      args[1] = url.replace("search_index.json", "search_index-" + locale + ".json");
    }
    return originalOpen.apply(this, args);
  };
})();
