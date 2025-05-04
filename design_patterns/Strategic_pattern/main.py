from design_patterns.Strategic_pattern.decoy_duck import Decoy_duck
from design_patterns.Strategic_pattern.mallar_duck import Mallar_duck
from design_patterns.Strategic_pattern.red_head_duck import Red_head_duck

if __name__ == '__main__':
    mallar_duck = Mallar_duck()
    mallar_duck.display()
    mallar_duck.swim()

    red_duck = Red_head_duck()
    red_duck.swim()
    red_duck.display()

    decoy = Decoy_duck()
    decoy.swim()