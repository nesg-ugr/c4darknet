interface CustomNode {
  id: string; // Cambiar el tipo a string
  label: string;
}

interface CustomLink {
  id: string;
  source: string;
  target: string;
  label?: string;
}
