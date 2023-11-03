def depthFirstSearch(problem):
    initialNode = problem.getStartState()
    if problem.isGoalState(initialNode): return []

    st = util.Stack()
    visitedList = []
    st.push((initialNode, []))

    while not st.isEmpty():
        initialNode, directions = st.pop()
        if initialNode not in visitedList:
            visitedList.append(initialNode)
            if problem.isGoalState(initialNode):
                return directions
            for nextNode, direction, cost in problem.getSuccessors(initialNode):
                nextAction = directions + [direction]
                st.push((nextNode, nextAction))