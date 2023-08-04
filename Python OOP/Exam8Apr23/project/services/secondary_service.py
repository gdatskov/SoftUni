from services.base_service import BaseService


class SecondaryService(BaseService):
    SERVICE_DEFAULT_CAPACITY = 15

    def details(self):
        """
        - Returns a string in the following format:
        "{service_name} Main Service:
        Robots: {robot_name1} {robot_name2} … {robot_nameN}"
        - If the service doesn't have any robots, add "none" instead of the robots' names:
        "{service_name} Main Service:
        Robots: none"
        """
        initial_string = f"{self.name} Secondary Service:" + "\n"
        robots_name_list = [robot.name for robot in self.robots]
        robots_string = " ".join(robots_name_list) if self.robots else "none"
        return initial_string + f"Robots: {robots_string}"

    def type(self):
        return "SecondaryService"

