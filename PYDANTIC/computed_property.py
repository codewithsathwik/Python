from pydantic import BaseModel,computed_field

class Bill(BaseModel):
    name : str
    room_id: int
    number_bookings : int
    price_room : float

    @computed_field
    @property
    def total_amt(self) -> float:
        return self.number_bookings * self.price_room
    

cus1 = Bill(
    name="sathwik", 
    room_id=101, 
    number_bookings=5, 
    price_room=500
)

print(cus1.total_amt)
print(cus1.model_dump())