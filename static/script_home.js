// Optional: Animate step entrance or highlight current step
document.addEventListener("DOMContentLoaded", () => {
  const steps = document.querySelectorAll('.step');
  steps.forEach((step, index) => {
    step.style.opacity = 0;
    setTimeout(() => {
      step.style.transition = "opacity 1s ease-in-out";
      step.style.opacity = 1;
    }, index * 300);
  });
});
