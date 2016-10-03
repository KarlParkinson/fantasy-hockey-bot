class rosterManager:

    def __init__(self):


    def setDailyRoster(self):
        readInRoster()
        filterByInjuries()
        filterByActive()
        rankRoster()
        setCenters()
        setLeftWing()
        setRightWing()
        setDefence()
        setGoalies()
