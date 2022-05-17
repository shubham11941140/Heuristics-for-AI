;; domain file: domain_logistics.pddl

(define (domain domain_logistics)

    ;; requirements
    (:requirements :strips :typing)


    ;; Types as mentioned in the problem
    ;; Places, cities and physical objects are considered as objects,
    ;; Packages and vehicles are physical objects,
    ;; Trucks and airplanes are vehicles,
    ;; Airports and locations are places.

    (:types city place physobj - object
            package vehicle - physobj
            truck airplane - vehicle
            airport location - place
    )


    ;; Predicates
    ;; in-city(loc, city) - true iff a place loc is in the city city
    ;; at(obj, loc) - true iff a physical object obj is at place loc
    ;; in(pkg, veh) - true iff the a package pkg is in a vehicle veh

    (:predicates 	(in-city ?loc - place ?city - city)
                        (at ?obj - physobj ?loc - place)
                        (in ?pkg - package ?veh - vehicle))


    ;; Load Truck Action
    ;; To load a truck, we need a package pkg and a truck truck at a place loc.
    ;; To load pkg in truck, these two objects must be at the same place loc.
    ;; The effects of loading pkg in truck are that in(pkg, truck) becomes true and at(pkg, loc) becomes false.
    ;; Any other fact in the current state does not change

    (:action load-truck
        :parameters (?pkg - package ?truck - truck ?loc - place)
        :precondition (and (at ?truck ?loc) (at ?pkg ?loc))
        :effect (and (not (at ?pkg ?loc)) (in ?pkg ?truck))
    )


    ;; Load Airplane Action
    ;; Description : Load a package pkg in an airplane airplane at a place loc,
    ;; Precondition : at(pkg, loc) and at(airplane, loc) must be true,
    ;; Effect : in(pkg, airplane) becomes true and at(airplane, loc) becomes false.

    (:action load-airplane
    :parameters (?pkg - package ?airplane - airplane ?loc - place)
    :precondition (and (at ?pkg ?loc) (at ?airplane ?loc))
    :effect (and (not (at ?pkg ?loc)) (in ?pkg ?airplane))
    )


    ;; Unload Truck Action
    ;; Description : Unload a package pkg in a truck truck at a place loc,
    ;; Precondition : in(pkg, truck) and at(truc, loc) must be true,
    ;; Effect : at(pkg, loc) becomes true and in(pkg, truck) becomes false.

    (:action unload-truck
    :parameters (?pkg - package ?truck - truck ?loc - place)
    :precondition (and (at ?truck ?loc) (in ?pkg ?truck))
    :effect (and (not (in ?pkg ?truck)) (at ?pkg ?loc))
    )


    ;; Unload Airplane Action
    ;; Description : Unload a package pkg in an airplane airplane at a place loc,
    ;; Precondition : in(pkg, airplane) and at(airplane, loc) must be true,
    ;; Effect : at(pkg, loc) becomes true and in(pkg, airplane) becomes false.

    (:action unload-airplane
    :parameters (?pkg - package ?airplane - airplane ?loc - place)
    :precondition (and (in ?pkg ?airplane) (at ?airplane ?loc))
    :effect (and (not (in ?pkg ?airplane)) (at ?pkg ?loc))
    )


    ;; Fly Airplane Action
    ;; Description : Fly airplane pkg from a location loc-from to a location loc-to,
    ;; Precondition : at(pkg, loc-from) must be true,
    ;; Effect : at(pkg, loc-to) becomes true and at(p, loc-from) becomes false.

    (:action fly-airplane
        :parameters (?airplane - airplane ?loc-from - airport ?loc-to - airport)
        :precondition (at ?airplane ?loc-from)
        :effect (and (not (at ?airplane ?loc-from)) (at ?airplane ?loc-to))
    )


    ;; Drive Truck Action
    ;; Description : Drive truck truck from a location loc-from to a location loc-to,
    ;; Precondition : at(truck, loc-from) must be true,
    ;; Effect : at(truck, loc-to) becomes true and at(truck, loc-from) becomes false.

    (:action drive-truck
    :parameters (?truck - truck ?loc-from - place ?loc-to - place ?city - city)
    :precondition (and (at ?truck ?loc-from) (in-city ?loc-from ?city) (in-city ?loc-to ?city))
    :effect (and (not (at ?truck ?loc-from)) (at ?truck ?loc-to))
    )

)
