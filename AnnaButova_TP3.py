from ui import AnimationMenuWindow
import animator

window = AnimationMenuWindow()
window.generate_button.clicked.connect(lambda:animator.animate_selected_objects(window))
window.show()