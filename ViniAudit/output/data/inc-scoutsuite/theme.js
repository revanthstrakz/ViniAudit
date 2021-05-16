const DARK_BOOTSTRAP_THEME = 'inc-bootstrap/css/bootstrap-dark.min.css';
const LIGHT_BOOTSTRAP_THEME = 'inc-bootstrap/css/bootstrap-light.min.css';

const DARK_Vini_THEME = 'inc-ViniAudit/css/ViniAudit-dark.css';
const LIGHT_Vini_THEME = 'inc-ViniAudit/css/ViniAudit-light.css';

$(document).ready(() => {
  if (isDarkThemeEnabled()) {
    document.getElementById('theme_checkbox').checked = true
  }
});

/**
 * Load the last theme used by looking into localstorage
 */
function loadLastTheme() {
  if (isDarkThemeEnabled()) {
    setBootstrapTheme(DARK_BOOTSTRAP_THEME)
    setViniTheme(DARK_Vini_THEME)
  }
}

/**
 * Toggles between light and dark themes
 */
function toggleTheme() {
  localStorage.setItem('dark_theme_enabled', document.getElementById('theme_checkbox').checked)
  if (document.getElementById('theme_checkbox').checked) {
    this.setBootstrapTheme(DARK_BOOTSTRAP_THEME)
    this.setViniTheme(DARK_Vini_THEME)
  }
  else {
    this.setBootstrapTheme(LIGHT_BOOTSTRAP_THEME)
    this.setViniTheme(LIGHT_Vini_THEME)
  }
};

/**
 * Toggles between light and dark themes
 */
function toggleTheme() {
  const darkThemeEnabled = document.getElementById('theme_checkbox').checked
  saveIsDarkThemeEnabled(darkThemeEnabled)

  if (darkThemeEnabled) {
    this.setBootstrapTheme(DARK_BOOTSTRAP_THEME)
    this.setViniTheme(DARK_Vini_THEME)
  }
  else {
    this.setBootstrapTheme(LIGHT_BOOTSTRAP_THEME)
    this.setViniTheme(LIGHT_Vini_THEME)
  }
};

/**
 * Sets the css file location received as the bootstrap theme
 * @param {string} file
 */
function setBootstrapTheme(file) {
  document.getElementById('bootstrap-theme').href = file
}

/**
 * Sets the css file location received as the Vini theme
 * @param {string} file
 */
function setViniTheme(file) {
  document.getElementById('Vini-theme').href = file
}

/**
 * Tells us if the dark theme is enabled or not
 * @returns {boolean}
 */
function isDarkThemeEnabled() {
  return localStorage.getItem('dark_theme_enabled') === 'true'
}

/**
 * Saves which theme is selected within the localstorage
 * @param {boolean} isDarkThemeEnabled 
 */
function saveIsDarkThemeEnabled(isDarkThemeEnabled) {
  localStorage.setItem('dark_theme_enabled', isDarkThemeEnabled)
}