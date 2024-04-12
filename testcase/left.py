def __call__(self, ax, renderer):
    # Subtracting transSubfigure will tipically rely on inverted(),
    # freezing the transform; thus, this needs to be delayed until draw
    # time as transSubfigure may otherwise change after this is evaluated.
    return mtransforms.TransformedBbox(
        mtransforms.Bbox.from_bounds(*self._bounds),
        a
        self._transform - ax.figure.transSubfigure)
