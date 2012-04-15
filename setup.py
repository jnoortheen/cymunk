from os.path import dirname, join
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

c_chipmunk_root = join(dirname(__file__), 'chipmunk', 'Chipmunk-Physics')
c_chipmunk_src = join(c_chipmunk_root, 'src')
c_chipmunk_incs = [join(c_chipmunk_root, 'include'),
        join(c_chipmunk_root, 'include', 'chipmunk')]
c_chipmunk_files = [join(c_chipmunk_src, x) for x in (
    'cpSpatialIndex.c', 'cpSpaceHash.c', 'constraints/cpPivotJoint.c',
    'constraints/cpConstraint.c', 'constraints/cpSlideJoint.c',
    'constraints/cpRotaryLimitJoint.c', 'constraints/cpGrooveJoint.c',
    'constraints/cpGearJoint.c', 'constraints/cpRatchetJoint.c',
    'constraints/cpSimpleMotor.c', 'constraints/cpDampedRotarySpring.c',
    'constraints/cpPinJoint.c', 'constraints/cpDampedSpring.c', 'cpSpaceStep.c',
    'cpArray.c', 'cpArbiter.c', 'cpCollision.c', 'cpBBTree.c', 'cpSweep1D.c',
    'chipmunk.c', 'cpSpaceQuery.c', 'cpBB.c', 'cpShape.c', 'cpSpace.c',
    'cpVect.c', 'cpPolyShape.c', 'cpSpaceComponent.c', 'cpBody.c',
    'cpHashSet.c')]

ext_modules = [
    Extension('chipmunk',
        ['chipmunk/python/chipmunk.pyx'] + c_chipmunk_files,
        include_dirs=c_chipmunk_incs,
        extra_compile_args=['-std=c99'],
        pyrex_directives={'embedsignature': True})]

setup(
    name='cymunk',
    description='Cython bindings for Chipmunk',
    author='Mathieu Virbel and Nicolas Niemczycki',
    author_email='mat@kivy.org',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules)