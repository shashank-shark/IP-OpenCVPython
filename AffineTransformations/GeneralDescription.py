# Before talking about affine transformations, let's learn what Euclidean transformations are.
# Euclidean transformations are a type of geometric transformation that preserve length and
# angle measures. If we take a geometric shape and apply Euclidean transformation to it, the
# shape will remain unchanged. It might look rotated, shifted, and so on, but the basic
# structure will not change. So technically, lines will remain lines, planes will remain planes,
# squares will remain squares, and circles will remain circles.
# Coming back to affine transformations, we can say that they are generalizations of
# Euclidean transformations. Under the realm of affine transformations, lines will remain
# lines, but squares might become rectangles or parallelograms. Basically, affine
# transformations don't preserve lengths and angles.In order to build a general affine transformation matrix, we need to define the control
# points. Once we have these control points, we need to decide where we want them to be
# mapped. In this particular situation, all we need are three points in the source image, and
# three points in the output image