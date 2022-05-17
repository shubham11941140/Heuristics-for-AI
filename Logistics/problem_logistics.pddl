;; problem file: problem_logstics.pddl

(define (problem problem_logistics)

;; domain file: domain_logistics.pddl

(:domain domain_logistics)

    ;; Object given
    ;; A Truck : truck
    ;; An airplane: airplane
    ;; Two airports : cdg, lhr
    ;; Two places : north, south
    ;; Two cities : london, paris
    ;; Two packages : p1, p2

    (:objects
      plane - airplane
      truck - truck
      cdg lhr - airport
      south north - location
      paris london - city
      p1 p2 - package)


	;; The initial state as a list of facts
	;; All facts are true
	;; All the facts that are not mentioned are false

    (:init (in-city cdg paris)
          (in-city lhr london)
          (in-city north paris)
          (in-city south paris)
          (at plane lhr)
          (at truck cdg)
          (at p1 lhr)
          (at p2 lhr)
    )


	;; The goal is to have at(p1, north) and at(p2, south) in the final state
	;; No matter the truth value of the other predicates.

    (:goal (and (at p1 north) (at p2 south)))

)
