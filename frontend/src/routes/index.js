// import pages
import Home from '../pages/Home/Home';
import Notfound from '../pages/Notfound/NotFound';

// import components
import { ProtectedRoute } from '../components/ProtectedRoute';

const AppRoutes = [
    { path: '/',
      element: <Home />
    },
    {
      path: '/not-found',
      element: <Notfound />
    },
    { 
      path: '*',
      element: <Notfound />
    }
  ]
  
  export default AppRoutes;