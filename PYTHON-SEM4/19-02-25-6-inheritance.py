# i - inheritance about latest model of apple iphone
class AppleIphone:
    def __init__(self, model, releaseyear):
        self.model = model
        self.releaseyear = releaseyear

class LatestIphone(AppleIphone):
    def __init__(self, model, releaseyear, features):
        super().__init__(model, releaseyear)
        self.features = features

# ii - inheritance about multiple autonomous colleges under a university
class University:
    def __init__(self, name):
        self.name = name

class AutonomousCollege(University):
    def __init__(self, name, collegename):
        super().__init__(name)
        self.collegename = collegename

# iii - multiple iits and nits under aicte
class AICTE:
    def __init__(self, name):
        self.name = name

class IIT(AICTE):
    def __init__(self, name, iitname):
        super().__init__(name)
        self.iitname = iitname

class NIT(AICTE):
    def __init__(self, name, nitname):
        super().__init__(name)
        self.nitname = nitname

# iv - inheritance about netflix membership
class NetflixMembership:
    def __init__(self, membershiptype):
        self.membershiptype = membershiptype

class PremiumMembership(NetflixMembership):
    def __init__(self, membershiptype, userwatching):
        super().__init__(membershiptype)
        self.userwatching = userwatching

    def checkaccess(self, usertryingtologin):
        if self.userwatching:
            print("Account is frozen for 24 hours due to multiple login attempts.")
        else:
            print("Access granted.")

# Example usage
latestiphone = LatestIphone("iPhone 13", 2021, ["5G", "A15 Bionic"])
print(f"Model: {latestiphone.model}, Release Year: {latestiphone.releaseyear}, Features: {latestiphone.features}")

college = AutonomousCollege("BPUT", "TRIDENT INSTITUTE OF TECHNOLOGY")
print(f"University: {college.name}, College: {college.collegename}")

iit = IIT("AICTE", "IIT Bombay")
print(f"AICTE: {iit.name}, IIT: {iit.iitname}")

nit = NIT("AICTE", "NIT Trichy")
print(f"AICTE: {nit.name}, NIT: {nit.nitname}")

premium = PremiumMembership("Premium", True)
premium.checkaccess("User2")
