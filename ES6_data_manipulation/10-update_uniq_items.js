export default function updateUniqueItems(groceries) {
  if (!(groceries instanceof Map)) {
    throw TypeError('Cannot process');
  }

  for (const [item, quantity] of groceries) {
    if (quantity === 1) {
      groceries.set(item, 100);
    }
  }

  return groceries;
}
