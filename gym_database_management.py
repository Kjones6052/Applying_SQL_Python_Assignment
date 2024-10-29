from add_gym_member import add_member
from add_workout_session import add_workout
from delete_workout import delete_workout
from update_member_age import update_member_age

# Adding a new member to the fitness center
add_member(5, "Coding Temple", 27)

# Adding a new workout for the new member
add_workout(5, 5, "2024-02-23", "12:00pm", "cycling")

# Updating the age of the new member
update_member_age(5, 32)

# Deleting the workout scheduled for the new member
delete_workout(5, 5)