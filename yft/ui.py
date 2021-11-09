import bpy


def draw_child_properties(layout, obj):
    layout.prop(obj.child_properties, "group_index")
    layout.prop(obj.child_properties, "bone_tag")
    layout.prop(obj.child_properties, "mass_1")
    layout.prop(obj.child_properties, "mass_2")
    layout.prop(obj.child_properties, "unk_vec")
    layout.prop(obj.child_properties, "inertia_tensor")


def draw_archetype_properties(layout, obj):
    layout.prop(obj.archetype_properties, "name")
    layout.prop(obj.archetype_properties, "mass")
    layout.prop(obj.archetype_properties, "mass_inv")
    layout.prop(obj.archetype_properties, "unknown_48")
    layout.prop(obj.archetype_properties, "unknown_4c")
    layout.prop(obj.archetype_properties, "unknown_50")
    layout.prop(obj.archetype_properties, "unknown_54")
    layout.prop(obj.archetype_properties, "inertia_tensor")
    layout.prop(obj.archetype_properties, "inertia_tensor_inv")


def draw_lod_properties(layout, obj):
    layout.prop(obj.lod_properties, "unk_14")
    layout.prop(obj.lod_properties, "unk_18")
    layout.prop(obj.lod_properties, "unk_1c")
    layout.prop(obj.lod_properties, "unk_30")
    layout.prop(obj.lod_properties, "unk_50")
    layout.prop(obj.lod_properties, "unk_60")
    layout.prop(obj.lod_properties, "unk_70")
    layout.prop(obj.lod_properties, "unk_80")
    layout.prop(obj.lod_properties, "unk_90")
    layout.prop(obj.lod_properties, "unk_a0")
    layout.prop(obj.lod_properties, "unk_b0")

    for idx, group in enumerate(obj.frag_group_properties):
        layout.label(text=f"Group {idx}")
        layout.prop(group, "name")
        layout.prop(group, "index")
        layout.prop(group, "parent_index")
        layout.prop(group, "unk_byte_4c")
        layout.prop(group, "unk_byte_4f")
        layout.prop(group, "unk_byte_50")
        layout.prop(group, "unk_byte_51")
        layout.prop(group, "unk_byte_52")
        layout.prop(group, "unk_byte_53")
        layout.prop(group, "unk_float_10")
        layout.prop(group, "unk_float_14")
        layout.prop(group, "unk_float_18")
        layout.prop(group, "unk_float_1c")
        layout.prop(group, "unk_float_20")
        layout.prop(group, "unk_float_24")
        layout.prop(group, "unk_float_28")
        layout.prop(group, "unk_float_2c")
        layout.prop(group, "unk_float_30")
        layout.prop(group, "unk_float_34")
        layout.prop(group, "unk_float_38")
        layout.prop(group, "unk_float_3c")
        layout.prop(group, "unk_float_40")
        layout.prop(group, "mass")
        layout.prop(group, "unk_float_54")
        layout.prop(group, "unk_float_58")
        layout.prop(group, "unk_float_5c")
        layout.prop(group, "unk_float_60")
        layout.prop(group, "unk_float_64")
        layout.prop(group, "unk_float_68")
        layout.prop(group, "unk_float_68")
        layout.prop(group, "unk_float_6c")
        layout.prop(group, "unk_float_70")
        layout.prop(group, "unk_float_74")
        layout.prop(group, "unk_float_78")
        layout.prop(group, "unk_float_a8")


def draw_fragment_properties(layout, obj):
    layout.label(text="fragment")
    layout.prop(obj.fragment_properties, "unk_b0")
    layout.prop(obj.fragment_properties, "unk_b8")
    layout.prop(obj.fragment_properties, "unk_bc")
    layout.prop(obj.fragment_properties, "unk_c0")
    layout.prop(obj.fragment_properties, "unk_c4")
    layout.prop(obj.fragment_properties, "unk_cc")
    layout.prop(obj.fragment_properties, "unk_d0")
    layout.prop(obj.fragment_properties, "unk_d4")