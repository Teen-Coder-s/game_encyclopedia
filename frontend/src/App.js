import React from 'react';
import { Route, Routes , Navigate } from 'react-router-dom';
import AppRoutes from './routes';

// import components

export default function App() {
    return (
        <>
            {/* <Header /> */}
            <Routes>
                {
                    AppRoutes.map((prop, key) => {
                        if (prop.redirect) {
                            return <Navigate key={key} from={prop.path} to={prop.pathTo} />
                        } else {
                            return <Route key={key} {...prop} />
                        }
                    })
                }
            </Routes>
            {/* <Footer /> */}
        </>
    )
}