from __future__ import annotations
from abc import ABC, abstractmethod


class ReportElement(ABC):
    def accept(self, visitor: ReportVisitor):
        visitor.visit(self)


class FixedPriceContract(ReportElement):
    def __init__(self, price_per_year: int):
        self.price_per_year = price_per_year


class TimeAndMaterialsContract(ReportElement):
    def __init__(self, cost_per_hour: int, hours: int):
        self.cost_per_hour = cost_per_hour
        self.hours = hours


class SupportContract(ReportElement):
    def __init__(self, cost_per_month: int):
        self.cost_per_month = cost_per_month


class ReportVisitor(ABC):
    @abstractmethod
    def visit_fpc(self, contract: FixedPriceContract):
        pass

    @abstractmethod
    def visit_tmc(self, contract: TimeAndMaterialsContract):
        pass

    @abstractmethod
    def visit_sc(self, contract: SupportContract):
        pass


class MonthlyCostReportVisitor(ReportVisitor):
    def visit_fpc(self, contract: FixedPriceContract):
        return contract.price_per_year / 12

    def visit_tmc(self, contract: TimeAndMaterialsContract):
        return contract.cost_per_hour * contract.hours

    def visit_sc(self, contract: SupportContract):
        return contract.cost_per_month


class YearlyCostReportVisitor(ReportVisitor):
    def visit_fpc(self, contract: FixedPriceContract):
        return contract.price_per_year

    def visit_tmc(self, contract: TimeAndMaterialsContract):
        return contract.cost_per_hour * contract.hours

    def visit_sc(self, contract: SupportContract):
        return contract.cost_per_month * 12


if __name__ == '__main__':
    project_alpha = FixedPriceContract(10000)
    project_beta = TimeAndMaterialsContract(150, 10)
    project_gamma = SupportContract(500)

    monthly_visitor = MonthlyCostReportVisitor()
    monthly_cost = monthly_visitor.visit_fpc(project_alpha)
    monthly_cost += monthly_visitor.visit_tmc(project_beta)
    monthly_cost += monthly_visitor.visit_sc(project_gamma)
    print(f"Monthly cost is: {monthly_cost}")

    yearly_visitor = YearlyCostReportVisitor()
    yearly_cost = yearly_visitor.visit_fpc(project_alpha)
    yearly_cost += yearly_visitor.visit_tmc(project_beta)
    yearly_cost += yearly_visitor.visit_sc(project_gamma)
    print(f"Yearly cost is: {yearly_cost}")
