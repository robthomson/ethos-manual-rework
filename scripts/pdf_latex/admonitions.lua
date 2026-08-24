-- Pandoc filter: renders the fenced Divs scripts/build_pdf_latex.py's
-- convert_admonitions() produces from mkdocs-material's `!!! type "title"`
-- syntax (e.g. `::: {.note}` ... `:::`) as colored boxes in the LaTeX
-- writer. Each Div carries exactly one class, equal to the admonition
-- type -- note/tip/warning/danger/example, matching
-- build_pdf_latex.py's ADMONITION_TYPES and the \definecolor names
-- ("admonNote", "admonTip", ...) its book_metadata() header-includes
-- defines. Any other Div (or any other output format) passes through
-- untouched.

local COLOR_FOR_CLASS = {
  note = "admonNote",
  tip = "admonTip",
  warning = "admonWarning",
  danger = "admonDanger",
  example = "admonExample",
}

function Div(el)
  if FORMAT ~= "latex" then
    return nil
  end
  for _, class in ipairs(el.classes) do
    local color = COLOR_FOR_CLASS[class]
    if color then
      local blocks = {}
      table.insert(
        blocks,
        pandoc.RawBlock(
          "latex",
          "\\begin{tcolorbox}[colframe=" .. color .. ",colback=" .. color
            .. "!5,boxrule=0.8pt,breakable]"
        )
      )
      for _, block in ipairs(el.content) do
        table.insert(blocks, block)
      end
      table.insert(blocks, pandoc.RawBlock("latex", "\\end{tcolorbox}"))
      return blocks
    end
  end
  return nil
end
