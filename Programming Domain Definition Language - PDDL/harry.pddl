(define (domain harry)
  (:requirements :strips :negative-preconditions :equality)
  (:predicates (atplace ?x)
                (placehas ?x ?y)
                (destroyed ?x)
                 (obtained ?x)
                 (candestroy ?x,?y)
                 (horcrux ?x)
                 (killed ?x))

  (:action pickup
           :parameters (?x ?y)
           :precondition (and (atplace ?x) (placehas ?x ?y))
           :effect (and (obtained ?y) (not (placehas ?x ?y))))

  (:action go
           :parameters (?x ?y)
           :precondition (and (atplace ?x) (not (atplace ?y)))
           :effect (and (atplace ?y) (not (atplace ?x))))

  (:action destroy
           :parameters (?x ?y)
           :precondition (and (obtained ?x) (obtained ?y) (horcrux ?y) (candestroy ?x ?y))
           :effect (and (destroyed ?y) 
                        ))

    (:action kill
        :parameters (?x ?y ?z ?a ?b)
        :precondition (and (atplace ?x) (placeHas ?x ?z) 
        (obtained ?y) (candestroy ?y ?z) (destroyed ?a) (destroyed ?b) (not (= ?a ?b)))
        :effect (and (killed ?z)))

) 