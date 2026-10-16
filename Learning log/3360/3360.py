"""BreadCut"""
def get_slice_sizes(cut, size):
    """BreadCut"""
    edges = [0] + cut + [size]
    return [b - a for a, b in zip(edges, edges[1:])]

def main():
    """CutBread"""
    w, h = map(int, input().split()[:2])
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    ws = sorted(get_slice_sizes(xs, w), reverse=True)
    heights = sorted(get_slice_sizes(ys, h), reverse=True)

    area = [ws[0] * heights[0]]
    if len(ws) > 1:
        area.append(ws[1] * heights[0])
    if len(heights) > 1:
        area.append(ws[0] * heights[1])
    area.sort(reverse=True)
    print(area[0], area[1] if len(area) > 1 else area[0])
main()
