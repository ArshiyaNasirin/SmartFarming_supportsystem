document.addEventListener("DOMContentLoaded", () => {
  const regionSelect = document.querySelector("[data-region-select]");
  const stateSelect = document.querySelector("[data-state-select]");

  if (!regionSelect || !stateSelect || !window.REGION_STATE_MAP) {
    return;
  }

  const selectedState = stateSelect.value;

  const renderStates = () => {
    const region = regionSelect.value;
    const states = window.REGION_STATE_MAP[region] || [];
    const currentState = stateSelect.value;

    stateSelect.innerHTML = "";
    states.forEach((stateName) => {
      const option = document.createElement("option");
      option.value = stateName;
      option.textContent = stateName;
      stateSelect.appendChild(option);
    });

    if (states.includes(currentState)) {
      stateSelect.value = currentState;
    } else if (states.includes(selectedState)) {
      stateSelect.value = selectedState;
    } else if (states.length > 0) {
      stateSelect.value = states[0];
    }
  };

  regionSelect.addEventListener("change", renderStates);
  renderStates();
});
