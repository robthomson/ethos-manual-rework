// Scopes Material's built-in search to the current page's language.
//
// mkdocs-static-i18n builds every locale into a single site, and Material's
// search plugin combines every locale's pages into one search_index.json
// (see mkdocs_static_i18n's plugin.reconfigure_search_index) -- so out of
// the box, searching from an English page also surfaces French/German/...
// results. There's no config knob for this -- see
// https://github.com/ultrabug/mkdocs-static-i18n/issues/271.
//
// This rewrites the one XHR Material's bundle.js makes for
// search_index.json to fetch hooks/split_search_index.py's split file
// matching the current URL's locale segment instead, before that request
// fires. overrides/main.html loads this script *before* bundle.js
// specifically so this patch is in place before that request goes out --
// see that file for why.
//
// The locale list below is patched in by hooks/split_search_index.py after
// the build; empty here is just the pre-patch default (e.g. during
// `mkdocs serve`), in which case this is a no-op and search falls back to
// the stock, unfiltered combined index.
(function () {
  var locales = /*__I18N_LOCALES__*/ ["de", "es", "it"];
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
