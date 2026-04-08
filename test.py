from tasks.easy_task import EasyTask
from tasks.medium_task import MediumTask
from tasks.hard_task import HardTask

# ----------------------------------------
# Simple dummy agent functions
# (just guesses the same answer every time)
# ----------------------------------------

# Easy agent — just says 'spam' always
def easy_agent(obs):
    return 'spam'

# Medium agent — says 'spam' + 'low' always
def medium_agent(obs):
    return 'spam', 'low'

# Hard agent — says 'spam' + 'low' + 'none' always
def hard_agent(obs):
    return 'spam', 'low', 'none'

# ----------------------------------------
# Run all 3 tasks
# ----------------------------------------
print('Running Easy Task...')
easy = EasyTask()
easy_result = easy.run(easy_agent)

print('Running Medium Task...')
medium = MediumTask()
medium_result = medium.run(medium_agent)

print('Running Hard Task...')
hard = HardTask()
hard_result = hard.run(hard_agent)

# ----------------------------------------
# Print final summary
# ----------------------------------------
print()
print('='*50)
print('📊 FINAL SUMMARY')
print('='*50)
print(f'🟢 Easy   Score: {easy_result["final_score"]:.2f}')
print(f'🟡 Medium Score: {medium_result["final_score"]:.2f}')
print(f'🔴 Hard   Score: {hard_result["final_score"]:.2f}')