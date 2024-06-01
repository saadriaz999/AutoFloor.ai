from src.shaz import MultiFloorPlanMaker


for i in range(1):
    Objs = MultiFloorPlanMaker.Get_MultFloor_List(2)
    MultiFloorPlanMaker.CreateMultiPlan(Objs[0],Objs[1])
