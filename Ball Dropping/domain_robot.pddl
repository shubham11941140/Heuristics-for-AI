;; domain file: domain_robot.pddl

(define (domain domain_robot)

    ;; requirements
    (:requirements :strips )

    ;; Predicates:
    ;; ROOM(x) – true iff x is a room
    ;; BALL(x) – true iff x is a ball
    ;; GRIPPER(x) – true iff x is a gripper (robot arm)
    ;; at-robby(x) – true iff x is a room and the robot is in x
    ;; at-ball(x, y) – true iff x is a ball, y is a room, and x is in y
    ;; free(x) – true iff x is a gripper and x does not hold a ball
    ;; carry(x, y) – true iff x is a gripper, y is a ball, and x holds y

    (:predicates (ROOM ?x) (BALL ?x) (GRIPPER ?x)
        (at-robby ?x)(at-ball ?x ?y)
        (free ?x) (carry ?x ?y))


    ;; Movement action:
    ;; Description: The robot can move from x to y.
    ;; Precondition: ROOM(x), ROOM(y) and at-robby(x) are true.
    ;; Effect: at-robby(y) becomes true. at-robby(x) becomes false.
    ;; Everything else doesn’t change.

        (:action move :parameters (?x ?y)
    :precondition (and (ROOM ?x) (ROOM ?y)
    (at-robby ?x))
    :effect (and (at-robby ?y)
    (not (at-robby ?x))))


    ;; Description: The robot can pick up x in y with z.
    ;; Precondition: BALL(x), ROOM(y), GRIPPER(z), at-ball(x, y), at-robby(y) and free(z) are true.
    ;; Effect: carry(z, x) becomes true. at-ball(x, y) and free(z) become false.
    ;; Everything else doesn’t change.

        (:action pick-up :parameters (?x ?y ?z)
    :precondition (and (BALL ?x) (ROOM ?y) (GRIPPER ?z)
    (at-ball ?x ?y) (at-robby ?y) (free ?z))
    :effect (and (carry ?z ?x)
    (not (at-ball ?x ?y)) (not (free ?z))))


    ;; Description: The robot can drop x in y from z.
    ;; Precondition: BALL(x), ROOM(y), GRIPPER(z), carry(z, x), at-robby(y) are true.
    ;; Effect: carry(z, x) becomes false. at-ball(x, y) and free(z) become true.
    ;; Everything else doesn’t change.

        (:action drop :parameters (?x ?y ?z)
    :precondition (and (BALL ?x) (ROOM ?y) (GRIPPER ?z)
    (carry ?z ?x) (at-robby ?y))
    :effect (and (at-ball ?x ?y) (free ?z)
    (not (carry ?z ?x))))

)
