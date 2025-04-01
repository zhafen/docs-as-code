import numpy as np

from . import data


class Framework:

    def complete_request(
        self, requester: data.Requester, request_concept: data.RequestConcept
    ) -> data.Report:

        request: data.Request = self.submit_intake_form(requester, request_concept)

        analyst: data.Analyst
        request, analyst = self.assign_request(request)

        report: data.Report = self.work_on_request(analyst, request)

        return report

    def submit_intake_form(self, requester: data.Requester, request_concept: data.RequestConcept) -> data.Request:
        pass

    def work_on_request(
        self,
        analyst: data.Analyst,
        request: data.Request,
        time_allotted: float = np.inf,
    ):
        """

        Parameters
        ----------
        analyst : data.Analyst
            _description_
        request : data.Request
            _description_
        """

        while request.time_spent < time_allotted:

            # Look up the status of the request
            request_status: str = request.get_status()

            if request_status == "new":
                request: data.Request = self.prepare_request_for_work(analyst, request)
            elif request_status == "in progress":
                request: data.Request = self.work_on_analysis(analyst, request, self.dt)
            elif request_status == "in review":
                request: data.Request = self.check_on_review_status(analyst, request)
            elif request_status == "closed":
                return request
            else:
                raise ValueError(f"Unexpected value, request_status={request_status}.")

            request.time_spent += self.dt
