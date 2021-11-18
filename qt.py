import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import requests

password_guess = st.text_input('What is the Password?') 
if password_guess != 'quantum': 
  st.stop()

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_wave = load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_lbHpNV.json')
st_lottie(lottie_wave, speed=1.5, width = 800, height = 400)

st.title('Quantum Theory')
st.write('by Me')
st.subheader('Question 1: ')
'''
1.1 The work function of barium and tungsten are 2.5 eV and 4.2 eV, respectively. Check whether
these materials are useful in a photocell, which is to be used to detect visible light.
'''

'''
Solution. The wavelength l of visible light is in the range 4000–7000 Å. Then,
'''

st.latex(r'Energy\hspace{0.1cm}of\hspace{0.1cm}4000\hspace{0.1cm}\mathop A\limits^o \hspace{0.1cm}light = \frac{{hc}}{\lambda } = \frac{{(6.626 \times {{10}^{ - 34}}Js)(3 \times {{10}^8}m/s)}}{{(4000 \times {{10}^{ - 10}}m)(1.6 \times {{10}^{ - 19}}J/eV)}} = 3.106eV')
st.latex(r'Energy\hspace{0.1cm}of\hspace{0.1cm}7000\hspace{0.1cm}\mathop A\limits^o \hspace{0.1cm}light = \frac{{hc}}{\lambda } = \frac{{(6.626 \times {{10}^{ - 34}}Js)(3 \times {{10}^8}m/s)}}{{(7000 \times {{10}^{ - 10}}m)(1.6 \times {{10}^{ - 19}}J/eV)}} = 1.77eV')

'''
The work function of tungsten is 4.2 eV, which is more than the energy range of visible light. Hence,
barium is the only material useful for the purpose.
'''
st.latex(r'\\')
st.latex(r'\\')
'''
2.18 Normalize the wave function ψ(x) = A exp (–ax^2
), A and a are constants, over the domain
– ∞ ≤ x ≤ ∞.

Solution. Taking A as the normalization constant, we get
'''
st.latex(r'{A^2}\int_{ - \infty }^\infty  {{\psi ^*}\psi dx = } {A^2}\int_{ - \infty }^\infty  {\exp ( - 2a{x^2})dx = 1}')
st.latex(r'\int_{ - \infty }^\infty  {{e^{ - 2a{x^2}}}dx, \hspace{0.5cm}} \int_{ - \infty }^\infty  {\int_{ - \infty }^\infty  {{e^{ - 2a{x^2} - 2a{y^2}}}dxdy} ,\hspace{0.5cm}} \int_{ - \infty }^\infty  {\int_{ - \infty }^\infty  {{e^{ - 2a{x^2}}}{e^{ - 2a{y^2}}}dxdy} ,} ')
st.latex(r'\int_{ - \infty }^\infty  {{e^{ - 2a{y^2}}}dy\int_{ - \infty }^\infty  {{e^{ - 2a{x^2}}}dx,\hspace{0.5cm}} I} \int_{ - \infty }^\infty  {{e^{ - 2a{y^2}}}dy = {I^2},} ')
st.latex(r'{I^2} = \int_{ - \infty }^\infty  {\int_{ - \infty }^\infty  {{e^{ - 2a{x^2} - 2a{y^2}}}dxdy} ,\hspace{0.5cm}} \int_0^\infty  {\int_0^{2\pi } {{e^{ - 2a{r^2}}}rd\theta d} r,} ')
st.latex(r'2\pi \int_0^\infty  {{e^{ - 2a{r^2}}}rdr,\hspace{0.5cm}u = }  - 2a{r^2},\hspace{0.5cm}du =  - 4ardr')
st.latex(r' - \frac{{2\pi }}{{4a}}\left. {{e^{ - 2a{r^2}}}} \right|_0^\infty  = \frac{\pi }{{2a}},\hspace{0.5cm}\therefore\hspace{0.5cm} I = \sqrt {\frac{\pi }{{2a}}} ')
st.latex(r'{A^2} = \frac{1}{{\sqrt {\frac{\pi }{{2a}}} }},\hspace{0.5cm}A = {\left( {\frac{{2a}}{\pi }} \right)^{1/4}}')
st.latex(r'\psi (x) = {\left( {\frac{{2a}}{\pi }} \right)^{1/4}}\exp ( - a{x^2})')

st.latex(r'\\')
st.latex(r'\\')

'''
2.19 A particle constrained to move along the x-axis in the domain 0 ≤ x ≤ L has a wave function
ψ(x) = sin (npx/L), where n is an integer. Normalize the wave function and evaluate the expectation
value of its momentum.
'''
'''
Solution. The normalization condition gives
'''
st.latex(r'{N^2}\int_0^L {{{\sin }^2}\frac{{n\pi x}}{L}dx = 1} ')
st.latex(r'{N^2}\int_0^L {\frac{1}{2}\left( {1 - \cos \frac{{2n\pi x}}{L}} \right)dx = 1} ')
st.latex(r'{N^2}\left[ {\frac{1}{2}\int_0^L {dx - \frac{1}{2}\int_0^L {\cos \frac{{2n\pi x}}{L}} dx} } \right] = 1,\hspace{1cm}{N^2}\left[ {\frac{1}{2}L - \frac{1}{2}\left( {\frac{L}{{2n\pi }}} \right)\sin \left. {\frac{{2n\pi x}}{L}} \right|_0^L} \right]')
st.latex(r'\frac{{{N^2}L}}{2} = 1,\hspace{1cm}N = \sqrt {\frac{2}{L}}')
'''
The normalized wave function is √(2/L) sin[(nπx)/L]. So,
'''
st.latex(r'\left\langle {{p_x}} \right\rangle  = \int_0^L {{\psi ^*}\left( { - i\hbar \frac{d}{{dx}}} \right)} \psi dx')
st.latex(r' \int_0^L {\sqrt {\frac{2}{L}} \sin \left( {\frac{{n\pi x}}{L}} \right) \cdot \left( { - i\hbar \frac{d}{{dx}}\sqrt {\frac{2}{L}} \sin \left( {\frac{{n\pi x}}{L}} \right)} \right)} dx')
st.latex(r'\frac{d}{{dx}}\left( {\sqrt {\frac{2}{L}} \sin \left( {\frac{{n\pi x}}{L}} \right)} \right) = \sqrt {\frac{2}{L}} \frac{{n\pi }}{L}\cos \frac{{n\pi x}}{L}')
st.latex(r'\int_0^L {\sqrt {\frac{2}{L}} \sin \left( {\frac{{n\pi x}}{L}} \right) \cdot \left( { - i\hbar \sqrt {\frac{2}{L}} \frac{{n\pi }}{L}\cos \frac{{n\pi x}}{L}} \right)} dx')
st.latex(r' - i\hbar \frac{2}{L}\frac{{n\pi }}{L}\int_0^L {\sin \left( {\frac{{n\pi x}}{L}} \right)} \cos \left( {\frac{{n\pi x}}{L}} \right)dx')
st.latex(r'\sin 2A = 2\sin A\cos A,\hspace{1cm} - i\hbar \frac{{2n\pi }}{{{L^2}}}\left( {\frac{1}{2}} \right)\int_0^L {\sin \frac{{2n\pi x}}{L}dx} ')
st.latex(r' - i\hbar \frac{{n\pi }}{{{L^2}}}\int_0^L {\sin \frac{{2n\pi x}}{L}dx}  = 0')

st.latex(r'\\')
st.latex(r'\\')

'''
2.20 Give the mathematical representation of a spherical wave travelling outward from a point and
evaluate its probability current density.
Solution. The mathematical representation of a spherical wave travelling outwards from a point is
given by
'''
st.latex(r'\psi (r) = \frac{A}{r}\exp (ikr)')
'''
where A is a constant and k is the wave vector. The probability current density
'''
st.latex(r'j = \frac{{i\hbar }}{{2m}}(\psi \nabla \psi * - \psi *\nabla \psi )')
st.latex(r' = \frac{{i\hbar }}{{2m}}{\left| A \right|^2}\left[ {\frac{{{e^{ikr}}}}{r}\nabla \left( {\frac{{{e^{ - ikr}}}}{r}} \right) - \frac{{{e^{ - ikr}}}}{r}\nabla \left( {\frac{{{e^{ikr}}}}{r}} \right)} \right]')
st.latex(r'\frac{{r( - ik{e^{ - ikr}}) - {e^{ - ikr}}}}{{{r^2}}} = \frac{{ - ik{e^{ - ikr}}}}{r} - \frac{{{e^{ - ikr}}}}{{{r^2}}}')
st.latex(r'\frac{{r(ik{e^{ikr}}) - {e^{ikr}}}}{{{r^2}}} = \frac{{ik{e^{ikr}}}}{r} - \frac{{{e^{ikr}}}}{{{r^2}}}')
st.latex(r'  = \frac{{i\hbar }}{{2m}}{\left| A \right|^2}\left[ {\frac{{{e^{ikr}}}}{r}\left( {\frac{{ - ik{e^{ - ikr}}}}{r} - \frac{{{e^{ - ikr}}}}{{{r^2}}}} \right) - \frac{{{e^{ - ikr}}}}{r}\left( {\frac{{ik{e^{ikr}}}}{r} - \frac{{{e^{ikr}}}}{{{r^2}}}} \right)} \right]')
st.latex(r' = \frac{{i\hbar }}{{2m}}{\left| A \right|^2}\left( { - \frac{{ik}}{{{r^2}}} - \frac{1}{{{r^3}}} - \frac{{ik}}{{{r^2}}} + \frac{1}{{{r^3}}}} \right)')
st.latex(r' = \frac{{i\hbar }}{{2m}}{\left| A \right|^2}\left( { - \frac{{2ik}}{{{r^2}}}} \right) = \frac{{\hbar k}}{{m{r^2}}}{\left| A \right|^2}')

st.latex(r'\\')
st.latex(r'\\')
st.latex(r'\\')

'''
The wave function of a particle of mass m moving in a potential V(x) is '''
st.latex(r'\Psi (x,t) = A\exp \left( { - ikt - \frac{{km}}{\hbar }{x^2}} \right)')
'''where A and k are constants. Find the explicit form of the potential V(x).'''

st.latex(r'\frac{{2\hbar kmx}}{{{\hbar ^2}}},\hspace{1cm}\frac{{\delta \Psi }}{{\delta x}} = A{e^{\left( { - ikt - \frac{{km}}{\hbar }{x^2}} \right)\left( { - \frac{{2\hbar kmx}}{{{\hbar ^2}}}} \right)}} = \Psi \left( { - \frac{{2kmx}}{\hbar }} \right)')
st.latex(r'\frac{{2\hbar km}}{{{\hbar ^2}}},\hspace{1cm}\frac{{{\partial ^2}\Psi }}{{\partial {x^2}}} = \Psi \left( { - \frac{{2km}}{\hbar }} \right) + \left( { - \frac{{2kmx}}{\hbar }} \right)\Psi \left( { - \frac{{2kmx}}{\hbar }} \right)')
st.latex(r' = \Psi \left( { - \frac{{2km}}{\hbar }} \right) + \left( {\frac{{4{k^2}{m^2}{x^2}}}{{{\hbar ^2}}}} \right)\Psi  = \left( { - \frac{{2km}}{\hbar } + \frac{{4{k^2}{m^2}{x^2}}}{{{\hbar ^2}}}} \right)\Psi ')
st.markdown("<h3 style='text-align: center; color: white;'>TDSE</h3>", unsafe_allow_html=True)
st.latex(r'i\hbar \frac{{\delta \Psi }}{{\delta t}} =  - \frac{{{\hbar ^2}}}{{2m}}\frac{{{\partial ^2}\Psi }}{{\partial {x^2}}} + V\Psi ,\hspace{1cm}i\hbar \frac{{\delta \Psi }}{{\delta t}} = k\hbar \Psi ')
st.latex(r'k\hbar \Psi  + \frac{{{\hbar ^2}}}{{2m}}\left( { - \frac{{2km}}{\hbar } + \frac{{4{k^2}{m^2}{x^2}}}{{{\hbar ^2}}}} \right)\Psi  = V\Psi ')
st.latex(r'k\hbar \Psi  - \frac{{2{\hbar ^2}km}}{{2m\hbar }}\Psi  + \frac{{4{\hbar ^2}{k^2}{m^2}{x^2}}}{{2m{\hbar ^2}}}\Psi  = V\Psi ')
st.latex(r'k\hbar \Psi  - k\hbar \Psi  + 2{k^2}m{x^2}\Psi  = V\Psi ')
st.latex(r'V(x) = 2{k^2}m{x^2}')


st.latex(r'\\')
st.latex(r'\\')

'''
2.22 The time-independent wave function of a system is
'''
st.latex(r'\psi (x) = A\exp (ikx)')
'''
where k is a constant.
Check whether it is normalizable in the domain –∞< x < ∞. Calculate the probability current density
for this function.
'''
'''
Solution. Substitution of ψ(x) in the normalization condition gives
'''
st.latex(r'\left| {{N^2}} \right|\int_{ - \infty }^\infty  {{{\left| \psi  \right|}^2}dx = } \left| {{N^2}} \right|\int_{ - \infty }^\infty  {{{\left| A \right|}^2}{{\mathop{\rm e}\nolimits} ^{2ikx}}dx} ')
st.latex(r'\frac{{\left| {{N^2}} \right|{{\left| A \right|}^2}}}{{2ik}}{{\mathop{\rm e}\nolimits} ^{2ikx}} = \left. {\frac{{\left| {{N^2}} \right|{{\left| A \right|}^2}}}{{2ik}}{{\mathop{\rm e}\nolimits} ^{2ikx}}} \right|_{ - \infty }^\infty  = 1')
'''
As this integral is not finite, the given wave function is not normalizable in the usual sense. The
probability current density
'''
st.latex(r'j = \frac{{i\hbar }}{{2m}}(\psi \nabla {\psi ^*} - {\psi ^*}\nabla \psi )')
st.latex(r'\frac{\delta }{{\delta x}}\left( {A{e^{ - ikx}}} \right) =  - A{e^{ - ikx}}(ik),{\hspace 1cm}\frac{\delta }{{\delta x}}\left( {A{e^{ikx}}} \right) = A{e^{ikx}}(ik)')
st.latex(r'A{e^{ikx}}( - A{e^{ - ikx}}(ik)) =  - {A^2}{e^{ikx}}{e^{ - ikx}}(ik),{\hspace 1cm}A{e^{ - ikx}}(A{e^{ikx}}(ik)) = {A^2}{e^{ - ikx}}{e^{ikx}}(ik)')
st.latex(r'\frac{{i\hbar }}{{2m}}( - {A^2}ik - {A^2}ik),\frac{{i\hbar }}{{2m}}{A^2}( - ik - ik),{\hspace 1cm}{A^2}\left( {\frac{{k\hbar }}{{2m}} + \frac{{k\hbar }}{{2m}}} \right),{\hspace 1cm}{A^2}\frac{{k\hbar }}{m}')
st.latex(r'\\')
st.latex(r'\\')

'''
2.27 The time-independent wave function of a particle of mass m moving in a potential V(x)= α²x² is
'''
st.latex(r'\psi (x) = \exp \underbrace {\left( {\sqrt {\frac{{m{\alpha ^2}}}{{2{\hbar ^2}}}} {x^2}} \right)}_u, {\hspace 0.1cm}\alpha {\hspace 0.1cm}being{\hspace 0.1cm}a{\hspace 0.1cm}constant')

'''
Find the energy of the system
'''
'''
Solution. We have
'''
st.latex(r'\frac{{du}}{{dx}} =  - 2x{\left( {\frac{{m{\alpha ^2}}}{{2{\hbar ^2}}}} \right)^{\frac{1}{2}}} =  - x\sqrt {\frac{{2m{\alpha ^2}}}{{{\hbar ^2}}}} ')
st.latex(r'\frac{{d\psi }}{{dx}} = {e^{\left( { - \sqrt {\frac{{m{\alpha ^2}}}{{2{\hbar ^2}}}} {x^2}} \right)}}\left( { - x\sqrt {\frac{{2m{\alpha ^2}}}{{{\hbar ^2}}}} } \right),')
st.latex(r'\frac{{{d^2}\psi }}{{d{x^2}}} = {e^{\left( { - \sqrt {\frac{{m{\alpha ^2}}}{{2{\hbar ^2}}}} {x^2}} \right)}} - \sqrt {\frac{{2m{\alpha ^2}}}{{{\hbar ^2}}}}  + \left( { - x\sqrt {\frac{{2m{\alpha ^2}}}{{{\hbar ^2}}}} } \right){e^{\left( { - \sqrt {\frac{{m{\alpha ^2}}}{{2{\hbar ^2}}}} {x^2}} \right)}}\left( { - x\sqrt {\frac{{2m{\alpha ^2}}}{{{\hbar ^2}}}} } \right)')
st.latex(r'')
