const wordReplacements = {
  "sum": "\\sum_{k}^{n}",
  "prod": "\\prod_{k}^{n}",
  "sqrt": "\\sqrt{a}",
  "integr": "\\int_{a}^{b}",
  "limit": "\\lim_{x \\to a}",
  "inf": "\\infty",
  "implique": "\\implies",
  "equivalent": "\\iff",
  "binom": "\\binom{n}{k}",
  "deriv": "\\dv{f}{x}",
  "inclue": "\\subset",
  "mat3": "\\begin{pmatrix}\r\n &  &  \\\\\r\n &  &  \\\\\r\n &  & \r\n\\end{pmatrix}",
  "mat2": "\\begin{pmatrix}\r\n &  \\\\\r\n & \r\n\\end{pmatrix}"
};

const keymap = {
  '<': { value: '<>', pos: 1 },
  '(': { value: '()', pos: 1 },
  '{': { value: '{}', pos: 1 },
  '[': { value: '[]', pos: 1 },
  '\'': { value: '\'\'', pos: 1 },
  '"': { value: '""', pos: 1 },
  '“': { value: '“”', pos: 1 },
  '`': { value: '``', pos: 1 },
  '‘': { value: '‘’', pos: 1 },
  '«': { value: '«»', pos: 1 },
  '「': { value: '「」', pos: 1 },
  '*': { value: '**', pos: 1 },
  '_': { value: '__', pos: 1 },
  '>': { value: '> ', pos: 2 },
  '~': { value: '~~', pos: 1 },
  '/': { value: '\\frac{}{}', pos: 6 },
  '$': { value: '$$', pos: 1 }
};

function setupInputBehavior(editing) {
  editing.addEventListener('keydown', event => {
    if (keymap[event.key]) {
      event.preventDefault();
      const pos = editing.selectionStart;
      editing.value = editing.value.slice(0, pos) +
                      keymap[event.key].value +
                      editing.value.slice(editing.selectionEnd);
      editing.selectionStart = editing.selectionEnd = pos + keymap[event.key].pos;
    }
  });

  editing.addEventListener('input', () => {
    const pos = editing.selectionStart;
    let text = editing.value;

    for (const [target, replacement] of Object.entries(wordReplacements)) {
      const regex = new RegExp(`\\b${target}\\b`, 'gi');
      text = text.replace(regex, replacement);
    }

    editing.value = text;
    editing.selectionStart = editing.selectionEnd = pos;
  });
}

// Initialise le comportement après que le DOM est chargé
window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('textarea').forEach(setupInputBehavior);
});



function save(){
  const matier = document.getElementById("Matier").value;
  const name = document.getElementById("Name").value;
  const question = document.getElementById("inputText").value;
  // const quest_img = document.getElementById("ques_imt").value;
  const quest_img = 0
  const rep = document.getElementById("input_rep").value;
  // const rep_img = document.getElementById("rep_imt").value;
  const rep_img = 0

  const data = {matier, name, question,quest_img,rep,rep_img};
  window.chrome.webview.postMessage(data);
}