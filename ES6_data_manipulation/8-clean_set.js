export default function cleanSet(Set, startString) {
  const cleanedValues = Array.from(Set)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');
  return cleanedValues;
}