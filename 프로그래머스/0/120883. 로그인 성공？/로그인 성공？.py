def solution(id_pw, db):
    for ddbb in db:
        if id_pw == ddbb:              
            return "login"
        elif id_pw[0] == ddbb[0]:     
            return "wrong pw"

    return "fail"                    
