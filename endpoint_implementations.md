# Implementation Endpoints Documentation

This document outlines the specific API endpoints responsible for the business logic implemented for Order Payments, Vendor Settlements, Warranty Limits, and Referral Programs.

---

## 1. Checkout & Transaction Splits

**Endpoint**: `POST /customers/checkout/`

*   **Role**: Handles the creation of the new `Transaction` and `TransactionItem` architecture.
*   **Logic Implemented**: 
    *   Ensures that payments are processed into the unified Saletick Paystack account.
    *   Automatically splits the cart items across multiple vendors (if applicable) using `TransactionItem` records, allowing separate tracking for each vendor's portion of the order.
    *   **Inventory Sync**: Upon successful payment, this process triggers a background task/signal to sync the purchased product quantities back to the main Saletick database.

---

## 2. Order Cancellation & Vendor Shipping Lock

**Endpoint**: `POST /customers/orders/<uuid:pk>/cancel/`

*   **Role**: Allows a customer to request cancellation of their order.
*   **Logic Implemented**: 
    *   The endpoint checks the current status of the order. 
    *   If the vendor has already initiated shipping (e.g., status is updated to `shipped` or `processing_for_delivery`), the API rejects the cancellation request and prevents the customer from abandoning the order mid-shipment.

---

## 3. Vendor Settlement Delay (8-Day Rule)

**Endpoint**: `POST /customers/orders/<uuid:pk>/confirm-delivery/`

*   **Role**: Allows the customer to manually mark the product as delivered upon receipt.
*   **Logic Implemented**: 
    *   Confirming delivery immediately updates the status of the associated `TransactionItem` records.
    *   This action acts as the primary trigger for Vendor Settlement. Vendor accounts cannot be credited until this endpoint is called **OR** a background process determines 8 days have passed without a complaint.

*(Note: The secondary fallback for settlement is handled by the Celery beat task `process-withdrawals-daily` which runs every midnight).*

---

## 4. Warranty & Complaint Time Limit (8-Day Rule)

**Endpoints**: 
*   `GET /customers/warranty-requests/` (List requests)
*   `POST /customers/warranty-requests/` (File a new complaint/warranty claim)

*   **Role**: Handles customer complaints and refund requests for purchased items.
*   **Logic Implemented**: 
    *   When creating a request via `POST`, the system validates the delivery date of the associated order.
    *   If more than 8 days have elapsed since the product was marked as delivered, the API strictly blocks the creation of the request, disabling refunds or complaints.

---

## 5. Dynamic Referral Programs

**Endpoints**: 
*   `GET /referrals/admin/commission-settings/`
*   `POST /referrals/admin/commission-settings/`
*   `PUT /referrals/admin/commission-settings/<uuid:pk>/`

*   **Role**: Manages the commission structures for the referral system.
*   **Logic Implemented**: 
    *   Allows Admins (and authorized Vendors) to define global referral rules.
    *   Supports dynamic overrides: Admins/Vendors can bypass standard rules to set custom commission percentages or flat-rate rewards for specific individual products.

---

## 6. API Documentation

**Endpoint**: `GET /docs/`

*   **Role**: Serves the interactive Swagger/OpenAPI documentation.
*   **Logic Implemented**: 
    *   Resolves previous `AssertionError` crashes caused by custom views (like webhooks) missing standard serializers. 
    *   Safely generates the schema for all 177+ active endpoints in the application.
