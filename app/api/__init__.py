from fastapi import APIRouter, Depends


# from app.api.v1 import r_root, system_setup, biz_setup
# from app.api.v2 import v2Router
# from app.api.v6 import v6Router
# from app.api.v7 import v7Router
# from app.api.vm import vmRouter
# from app.api.ocr import ocrRouter
# from app.api.erp import erpRouter
# from app.api.sync import syncRouter

rou = APIRouter()

# rou.include_router(v7Router)
# rou.include_router(syncRouter)
# rou.include_router(erpRouter)
# rou.include_router(vmRouter)
# rou.include_router(ocrRouter)
# rou.include_router(v2Router)
# rou.include_router(r_root.router, tags=["Root"], dependencies=[Depends(authent)])
# rou.include_router(system_setup.router, prefix="/system_setup",tags=["System Setup"], dependencies=[Depends(authent)])
# rou.include_router(biz_setup.router,prefix="/biz_setup",tags=["BizEntity Setup"], dependencies=[Depends(authent)],)
