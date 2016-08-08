# my calculator
# a custom module containing all my favourite eqns

def Re(U, D, *fluid, **kwarg):
    """
    Re Calculator, mandatory arguments U, D
    fluid properties mu and rho can be inputted explicitly
    e.g.
    -----------------------------
    Re(U=5, D=2, rho=5, mu=21)
    ------------------------------
    if U, D are only specified then default values of 
    mu = 1e-3; rho = 998; are used
    -----------------------------
    Re(5,2)
    Re(D=2,U=5)
    -----------------------------
    
    Fluid properties can be defined by its fluid name (only water or air)
    and its temperature. Its mu and rho is then interpolated from tables    
    e.g. 
    -----------------------------
    Re(5,2, 'water', 20)
    -----------------------------
    """
    if len(fluid) > 0:
        # Check what fluid is selected
        if fluid[0] == 'water':
            print('Water at %db degrees ' %fluid[1])
            print('has rho=998kg/m3 and mu = 1e-3kg/ms')
            rho = 998
            mu = 1e-3
            
        if fluid[0] == 'air':
            print('Air at %db degrees ' %fluid[1])
            print('has rho=998kg/m3 and mu = 1e-3kg/ms')
            rho = 998
            mu = 1e-3
    else:
        # default values are usedbased on water @20oC
        mu = 1e-3
        rho = 998
        print('default values are used')
        
                 
    Re = rho * U * D / mu
    return(Re)

    
def massFR(rho, U, A):
    mFR = rho*U*A
    return(mFR)
    
def speak():
    import random
    nouns = ('Damon', 'Pedro','Robert','Anton', 'Nicholas','Alex','Deakin','Peter','Harrison','Rachael','Edward', 'Stuart', 'Ruth', 'Michael','John')
    verbs = ('applauds','appreciates','approves','argues', 'arranges', 'calculates','supports','scrapes','cares','talks','carves','causes','tumbles','sleeps', 'twists') 
    adv = ('crazily.', 'dutifully.', 'foolishly.', 'merrily.', 'occasionally.', 'unbelievably.', 'compassionately.','delicately.', 'cautiously.','eagerly.','diligently.', 'ethically.','intelligently.', 'hastily.', 'joyfully.')
    num = random.randrange(0,15)
    print (nouns[num] + ' ' + verbs[num] + ' ' + adv[num])