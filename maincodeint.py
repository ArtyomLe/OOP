
from codeint import CodeInt

score = CodeInt(100)
enemy_kill_score = CodeInt(50)
score.digit = score.code(int(score) + int(enemy_kill_score))
print(score)