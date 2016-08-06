(require 'package "package")

(in-package #:icfp-2016)

(defstruct origami
  (vertices nil :type 'list)
  (edges nil :type 'lits))

(defstruct point
  (x 0 :type 'number)
  (y 0 :type 'number))

(defstruct line
  (a nil :type 'point)
  (b nil :type 'point))



(provide 'struct)
