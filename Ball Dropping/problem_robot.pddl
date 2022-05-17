;; problem file: problem_robot.pddl

(define (problem problem_robot)

;; domain file: domain_robot.pddl

(:domain domain_robot)

    ;; Objects:
    ;; Rooms: rooma, roomb
    ;; Balls: ball1, ball2, ... ball8
    ;; Robot arms: left, right

    (:objects rooma roomb
    ball1 ball2 ball3 ball4 ball5 ball6 ball7 ball8
    left right)


    ;; Initial state:
    ;; ROOM(rooma) and ROOM(roomb) are true.
    ;; BALL(ball1), ..., BALL(ball8) are true.
    ;; GRIPPER(left), GRIPPER(right), free(left) and free(right) are true.
    ;; at-robby(rooma), at-ball(ball1, rooma), ..., at-ball(ball8, rooma) are true.
    ;; Everything else is false.

    (:init (ROOM rooma) (ROOM roomb)
    (BALL ball1) (BALL ball2) (BALL ball3) (BALL ball4) (BALL ball5) (BALL ball6) (BALL ball7) (BALL ball8)
    (GRIPPER left) (GRIPPER right) (free left) (free right)
    (at-robby rooma)
    (at-ball ball1 rooma) (at-ball ball2 rooma)
    (at-ball ball3 rooma) (at-ball ball4 rooma)
    (at-ball ball5 rooma) (at-ball ball6 rooma)
    (at-ball ball7 rooma) (at-ball ball8 rooma))


    ;; Goal state:
    ;; at-ball(ball1, roomb), ..., at-ball(ball8, roomb) must be true..

    (:goal (and (at-ball ball1 roomb)
    (at-ball ball2 roomb)
    (at-ball ball3 roomb)
    (at-ball ball4 roomb)
    (at-ball ball5 roomb)
    (at-ball ball6 roomb)
    (at-ball ball7 roomb)
    (at-ball ball8 roomb)))

)
