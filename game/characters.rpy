transform sprites_default:
    align (0.55, -0.07)


define config.tag_transform["yanatest"] = sprites_default

layeredimage yanatest:

    at Flatten

    # cabeza
    group head:
        attribute h_base default:
            # offset (0.6, 1)
            "sans/yanatest/head_base.png"


    # cuerpo izquierda
    group lbody:
        # xoffset (1)
        attribute base default:
            "sans/yanatest/body_base_left_a.png"
        attribute uniform:
            "sans/yanatest/body_uniform_left_a.png"

    # cuerpo derecha
    group rbody:
        attribute base default:
            "sans/yanatest/body_base_right_a.png"
        attribute uniform:
            "sans/yanatest/body_uniform_right_a.png"