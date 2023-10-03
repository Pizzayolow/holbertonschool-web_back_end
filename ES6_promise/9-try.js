export default function guardrail(mathFunction) {
  const queue = [];
  const errorMsg = 'Guardrail was processed';
  try {
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    queue.push(`Error: ${error.message}`);
  } finally {
    queue.push(errorMsg);
  }
  return queue;
}
