import bpy
import bmesh



class LinesDxfExport():
	def __init__(self):
		pass

	def export(self, filename):
		lines = self._get_lines()
		content = self._gen_dxf(lines)

		with open(filename, 'w') as f:
			f.write(content)


	def _get_lines(self):
		bm = bmesh.from_edit_mesh(bpy.context.object.data)
		lines = []
		for e in bm.edges:
			if e.select:
				line = []
				for v in e.verts:
					line.append(v.co)
				lines.append(line)
		return lines

	def _gen_dxf(self, lines):
		header = "0\nSECTION\n2\nENTITIES"
		footer = "0\nENDSECT\n0\nEOF"

		line_fmt = "\n0\nLINE\n8\n0\n10\n{}\n20\n{}\n30\n{}\n11\n{}\n21\n{}\n31\n{}"

		content = ""


		for line in lines:
			if len(line) == 2:
				x1 = round(line[0][0], 3)
				y1 = round(line[0][1], 3)
				z1 = round(line[0][2], 3)

				x2 = round(line[1][0], 3)
				y2 = round(line[1][1], 3)
				z2 = round(line[1][2], 3)
				content += line_fmt.format(x1, y1, 0, x2, y2, 0)

		return header + content + footer
		print(header + content + footer)