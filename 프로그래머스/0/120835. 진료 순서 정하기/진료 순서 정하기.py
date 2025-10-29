def solution(emergency):
    st = sorted(emergency, reverse=True)
    return [st.index(i)+1 for i in emergency ]