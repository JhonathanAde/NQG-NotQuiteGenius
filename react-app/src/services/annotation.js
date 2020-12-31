export const getAnnotations = async (id) => {
  const response = await fetch(`/api/users/${id}/annotations`)
  return await response.json();
}