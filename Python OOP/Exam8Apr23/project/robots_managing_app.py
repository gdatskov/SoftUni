from robots.base_robot import BaseRobot
from robots.female_robot import FemaleRobot
from robots.male_robot import MaleRobot
from services.base_service import BaseService
from services.main_service import MainService
from services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type, name):
        if service_type == "MainService":
            service = MainService(name)
        elif service_type == "SecondaryService":
            service = SecondaryService(name)
        else:
            raise Exception("Invalid service type!")

        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type == "MaleRobot":
            robot = MaleRobot(name, kind, price)
        elif robot_type == "FemaleRobot":
            robot = FemaleRobot(name, kind, price)
        else:
            raise Exception("Invalid robot type!")

        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot: BaseRobot = self.__get_robot_by_name(robot_name)
        service: BaseService = self.__get_service_by_name(service_name)

        valid_male_robot_assignment = robot.type() == "MaleRobot" and service.type() == "MainService"
        valid_female_robot_assignment = robot.type() == "FemaleRobot" and service.type() == "SecondaryService"

        if valid_male_robot_assignment or valid_female_robot_assignment:
            if not service.capacity_reached:
                service.robots.append(robot)
                self.robots.remove(robot)
                return f"Successfully added {robot_name} to {service_name}."
            else:
                raise Exception("Not enough capacity for this robot!")
        else:
            return "Unsuitable service."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        robot: BaseRobot = self.__get_robot_by_name(robot_name)
        service: BaseService = self.__get_service_by_name(service_name)

        if robot not in service.robots:
            raise Exception("No such robot in this service!")
        else:
            service.robots.remove(robot)
            self.robots.append(robot)
            return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service: BaseService = self.__get_service_by_name(service_name)
        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service: BaseService = self.__get_service_by_name(service_name)
        total_price = sum([robot.price for robot in service.robots])
        return f"The value of service {service_name} is {total_price}."

    def __get_robot_by_name(self, robot_name):
        robot = [robo for robo in self.robots if robo.name == robot_name]
        return robot[0] if robot else None

    def __get_service_by_name(self, service_name):
        service = [s for s in self.services if s.name == service_name]
        return service[0] if service else None

    def __str__(self):
        return "\n".join([service.details() for service in self.services])
