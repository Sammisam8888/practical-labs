# i - inheritance about latest model of apple iphone
class AppleIphone:
    def __init__(self, model, release_year):
        self.model = model
        self.release_year = release_year

class LatestIphone(AppleIphone):
    def __init__(self, model, release_year, features):
        super().__init__(model, release_year)
        self.features = features

# ii - inheritance about multiple autonomous colleges under a university
class University:
    def __init__(self, name):
        self.name = name

class AutonomousCollege(University):
    def __init__(self, name, college_name):
        super().__init__(name)
        self.college_name = college_name

# iii - multiple iits and nits under aicte
class AICTE:
    def __init__(self, name):
        self.name = name

class IIT(AICTE):
    def __init__(self, name, iit_name):
        super().__init__(name)
        self.iit_name = iit_name

class NIT(AICTE):
    def __init__(self, name, nit_name):
        super().__init__(name)
        self.nit_name = nit_name

# iv - inheritance about netflix membership
class NetflixMembership:
    def __init__(self, membership_type):
        self.membership_type = membership_type

class PremiumMembership(NetflixMembership):
    def __init__(self, membership_type, user_watching):
        super().__init__(membership_type)
        self.user_watching = user_watching

    def check_access(self, user_trying_to_login):
        if self.user_watching:
            print("Account is frozen for 24 hours due to multiple login attempts.")
        else:
            print("Access granted.")

# Example usage
latest_iphone = LatestIphone("iPhone 13", 2021, ["5G", "A15 Bionic"])
print(f"Model: {latest_iphone.model}, Release Year: {latest_iphone.release_year}, Features: {latest_iphone.features}")

college = AutonomousCollege("XYZ University", "ABC College")
print(f"University: {college.name}, College: {college.college_name}")

premium = PremiumMembership("Premium", True)
premium.check_access("User2")
